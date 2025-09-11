import os
import sqlite3
from tracker import storage, core

TEST_DB = "test_hourtracker.db"


def setup_module(module):
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    storage.DB_FILE = TEST_DB
    storage.init_db()


def test_start_and_stop():
    core.start_project("Projeto Teste")
    core.stop_project("Projeto Teste")
    report = core.generate_report()
    assert "Projeto Teste" in report
    assert report["Projeto Teste"] >= 0


def teardown_module(module):
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
