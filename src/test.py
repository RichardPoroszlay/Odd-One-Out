import unittest
import os
import logging.config
from flask import Flask, request
from app import app, db_conn, solution, rounds_to_play, rounds_won, rounds_lost, hc_score, get_solution
from unittest.mock import patch

def clear_log_file():
        if os.path.exists('test.log'):
            os.remove('test.log')

class TestAppRoutes(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.configure_logging()
        
    def configure_logging(self):
        logging.basicConfig(filename='test.log', level=logging.INFO)

    def log_test_start(self, test_name):
        logging.info(f"Starting test: {test_name}")

    def log_test_passed(self, test_name):
        logging.info(f"Test passed: {test_name}")

    def log_test_failed(self, test_name):
        logging.error(f"Test failed: {test_name}")

    def test_input_route(self):
        self.log_test_start("test_input_route")
        response = self.app.get('/input')
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_input_route")

    def test_input_game_route_GET(self):
        self.log_test_start("test_input_game_route_GET")
        response = self.app.get('/input_game')
        self.assertEqual(response.status_code, 302)
        self.log_test_passed("test_input_game_route_GET")

    def test_input_game_route_POST_invalid_rounds(self):
        self.log_test_start("test_input_game_route_POST_invalid_rounds")
        response = self.app.post('/input_game', data={'rounds': '0'})
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_input_game_route_POST_invalid_rounds")

    def test_input_game_route_POST_valid_rounds(self):
        self.log_test_start("test_input_game_route_POST_valid_rounds")
        response = self.app.post('/input_game', data={'rounds': '5'})
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_input_game_route_POST_valid_rounds")

    def test_input_game_route_POST_play_rounds(self):
        self.log_test_start("test_input_game_route_POST_play_rounds")
        response = self.app.post('/input_game', data={'rounds': '5'})
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/input_game')
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_input_game_route_POST_play_rounds")

    def test_input_game_id_route_correct_solution(self):
        self.log_test_start("test_input_game_id_route_correct_solution")
        response = self.app.get('/input_game/your_solution_id')
        self.assertEqual(response.status_code, 302)
        self.log_test_passed("test_input_game_id_route_correct_solution")

    def test_input_game_id_route_incorrect_solution(self):
        self.log_test_start("test_input_game_id_route_incorrect_solution")
        response = self.app.get('/input_game/incorrect_solution_id')
        self.assertEqual(response.status_code, 302)
        self.log_test_passed("test_input_game_id_route_incorrect_solution")

    def test_game_result_route(self):
        self.log_test_start("test_game_result_route")
        response = self.app.get('/game_result')
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_game_result_route")

    def test_store_result_route_correct_solution(self):
        self.log_test_start("test_store_result_route_correct_solution")
        response = self.app.get('/input_game/your_solution_id')
        self.assertEqual(response.status_code, 302)
        response = self.app.get('/input_game')
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_store_result_route_correct_solution")

    def test_store_result_route_incorrect_solution(self):
        self.log_test_start("test_store_result_route_incorrect_solution")
        response = self.app.get('/input_game/incorrect_solution_id')
        self.assertEqual(response.status_code, 302)
        response = self.app.get('/input_game')
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_store_result_route_incorrect_solution")

    def test_hardcore_route(self):
        self.log_test_start("test_hardcore_route")
        response = self.app.get('/hardcore')
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_hardcore_route")

    def test_show_next_route_correct_solution(self):
        self.log_test_start("test_show_next_route_correct_solution")
        response = self.app.get('/show_next/your_solution_id')
        self.assertEqual(response.status_code, 404)
        self.log_test_passed("test_show_next_route_correct_solution")

    def test_show_next_route_incorrect_solution(self):
        self.log_test_start("test_show_next_route_incorrect_solution")
        response = self.app.get('/show_next/incorrect_solution_id')
        self.assertEqual(response.status_code, 404)
        self.log_test_passed("test_show_next_route_incorrect_solution")

    def test_show_next_route_hc_score_reset(self):
        self.log_test_start("test_show_next_route_hc_score_reset")
        global hc_score
        response = self.app.get('/hardcore')
        hc_score = 5
        self.assertEqual(response.status_code, 200)
        self.log_test_passed("test_show_next_route_hc_score_reset")

    def test_hardcore_route_score(self):
        self.log_test_start("test_hardcore_route_score_tozero")
        response = self.app.get('/hardcore')
        hc_score = 0
        self.assertEqual(response.status_code, 200)
        self.log_test_start("test_hardcore_route_score_tozero")

    def test_show_next_route_incorrect_solution(self):
        self.log_test_start("test_show_next_route_incorrect_solution")
        global hc_score
        hc_score = 0  
        app.solution = "test_word"
        response = self.app.get('/hardcore/incorrect_solution_id')
        self.assertEqual(response.status_code, 200)
        self.log_test_start("test_show_next_route_incorrect_solution")

    def test_hardcore_route_zero(self):
        self.log_test_start("test_hardcore_route_zero")
        global hc_score
        hc_score = 0
        app.solution = "test_word"
        response = self.app.get('/hardcore')
        self.assertEqual(response.status_code, 200)
        self.log_test_start("test_hardcore_route_zero")

    def test_hardcore_route_nonzero_score(self):
        self.log_test_start("test_hardcore_route_nonzero_score")
        global hc_score
        hc_score = 5
        app.solution = "test_word"
        response = self.app.get('/hardcore')
        self.assertEqual(response.status_code, 200)
        self.log_test_start("test_hardcore_route_nonzero_score")

    def test_get_solution_2(self):
        self.log_test_start("test_hardcore_route_nonzero_score2")
        solution
        words = ["a"]
        self.assertEqual(get_solution(words), None)
        self.log_test_start("test_hardcore_route_nonzero_score2")

    def test_get_hc_score(self):
        self.log_test_start("test_get_hc_score")
        hc_score
        self.assertEqual(hc_score, 0)
        self.log_test_start("test_get_hc_score")  

    def test_get_rounds_to_play(self):
        self.log_test_start("test_get_rounds_to_play")
        rounds_to_play
        self.assertEqual(rounds_to_play, 0)
        self.log_test_start("test_get_rounds_to_play")

    

if __name__ == '__main__':
    clear_log_file()
    unittest.main()
