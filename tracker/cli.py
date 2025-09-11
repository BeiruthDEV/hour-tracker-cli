import argparse
from tracker.models import start_session, stop_session, report_sessions

def main():
    parser = argparse.ArgumentParser(description="Hour Tracker - Controle de horas com SQLite")
    subparsers = parser.add_subparsers(dest="command")

    # start
    start_parser = subparsers.add_parser("start", help="Inicia uma nova sessão de trabalho")
    start_parser.add_argument("--task", required=True, help="Nome da tarefa ou projeto")

    # stop
    subparsers.add_parser("stop", help="Finaliza a última sessão em aberto")

    # report
    subparsers.add_parser("report", help="Mostra o relatório de sessões registradas")

    args = parser.parse_args()

    if args.command == "start":
        start_session(args.task)
    elif args.command == "stop":
        stop_session()
    elif args.command == "report":
        report_sessions()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
