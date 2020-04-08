from os.path import dirname, join, abspath
from pyrep import PyRep
from pyrep.robots.arms.panda import Panda
from pyrep.robots.end_effectors.panda_gripper import PandaGripper
from pyrep.errors import ConfigurationPathError
# from Design_AIR_vrep import Scene, Robot, Camera
from pyrep.objects.shape import Shape
import numpy as np
import cv2 
import os
from Tic_tac_toe import Board, tictactoe_ai

chess_num = {'X':1,'O':1}
def next_chess(chess_type):
    global chess_num
    cube = Shape(f'chess_{chess_type}{chess_num[chess_type]}')
    print(f'chess_{chess_type}{chess_num[chess_type]}')
    chess_num[chess_type] += 1
    return cube

def chessboard_position(action):
    a = 0.06*np.array([[[-1,-1], [-1,0], [-1,1]],
                        [[0,-1],  [0,0],  [0,1]],
                        [[1,-1],  [1,0],  [1,1]]]).reshape((-1,2))[action]
    return [0.4+a[0], 0+a[1], 1.03]

if __name__ == "__main__":
    SCENE_FILE = join(dirname(abspath(__file__)), 'ttt.ttt')
    pr = PyRep()
    pr.launch(SCENE_FILE, headless=False,responsive_ui=True)
    panda = Panda()
    gripper = PandaGripper()
    pr.start()
    
    # Create Board instance
    os.system('clear')
    # home robot
    board = Board()
    # start
    input('Press enter to start')
    # Decide who first (X always first)
    instream = input('Do you want to play first hand?[y/n]')
    if instream != 'n':
        ai = tictactoe_ai('O')
        player_chess = 'X'
        Ai_chess = 'O'
        turn = 'player'
    else:
        ai = tictactoe_ai('X')
        player_chess = 'O'
        Ai_chess = 'X'
        turn = 'AI'

    # mian game loop
    while True:
        os.system('clear')
        print(f'You = {player_chess}\tAi = {Ai_chess}\n')
        board.print_board()
        print('')
        res = board.get_winner()
        if res == 0:
            # X win
            winner = 'X'
            if player_chess == 'X':
                print('you win')
            else:
                print('you lose')
            break
        elif res == 1:
            # O win
            winner = 'O'
            if player_chess == 'O':
                print('you win')
            else:
                print('you lose')
            break
        elif res == 2:
            # check is avalible
            if not board.check_avalible_action():
                winner = 'no'
                print('no one win')
                break

        if turn == 'player':
            # print board
            # input a number to play chess
            # | 0 1 2 |
            # | 3 4 5 |
            # | 6 7 8 |
            instream = input('Play(input a integer):')
            action = int(instream)
            if not board.is_legal_action(action) and action not in [0,1,2,3,4,5,6,7,8]:
                continue
            board._move(action,player_chess)
            # move player chess to chess board
            chess = next_chess(player_chess)
            chess.set_position(chessboard_position(action))
            pr.step()
            turn = "AI"

        elif turn == "AI":
            # think
            action = ai.think(board)
            # get AI chess
            chess = next_chess(Ai_chess)
            # get chess position
            pos = chess.get_position()
            pos[2] -= 0.01
            path = panda.get_path(position=pos,
                             euler=[0,np.pi,0])
            done = False
            while not done:
                done = path.step()
                pr.step()
            '''
            pos[2] -= 0.02
            path = panda.get_path(position=pos,
                             euler=[0,np.pi,0])
            done = False
            while not done:
                done = path.step()
                pr.step()
            '''
            
            gripper.grasp(chess)
            pr.step()
            '''
            input('go')
            while not gripper.actuate(0.5, 0.4):
                pr.step()
            gripper.grasp(chess)
            pr.step()
            '''

            pos[2] += 0.05
            path = panda.get_path(position=pos,
                             euler=[0,np.pi,0])
            done = False
            while not done:
                done = path.step()
                pr.step()

            pos = chessboard_position(action)
            pos[2] += 0.05
            path = panda.get_path(position=pos,
                             euler=[0,np.pi,0])
            done = False
            while not done:
                done = path.step()
                pr.step()
            
            while not gripper.actuate(1.0, 0.1):
                pr.step()
            gripper.release()
            pr.step()

            path = panda.get_path(position=[0.2, 0, 1.5],
                             euler=[0,np.pi,0])
            done = False
            while not done:
                done = path.step()
                pr.step()
            board._move(int(action),Ai_chess)
            turn = 'player'

    pr.stop()
    pr.shutdown()
    '''
    panda.move_p([0.7,0,0.3],[0,np.pi,0])
    panda.gripper_grasp(0.1)
    img = cam.bgr_image()
    
    '''
