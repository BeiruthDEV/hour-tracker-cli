import argparse
from models import start_session, stop_session, report_sessions
from db import init_db

def main():
    parser = argparse.ArgumentParser(description="HourTracker - Controlador de Horas")
    subparsers = parser.add_subparsers(dest="command")

    start_cmd = subparsers.add_parser("start", help="Inicia uma sessão")
    start_cmd.add_argument("project", help="Nome do projeto")

    stop_cmd = subparsers.add_parser("stop", help="Finaliza uma sessão")
    stop_cmd.add_argument("project", help="Nome do projeto")

    subparsers.add_parser("report", help="Mostra relatório de horas")

    args = parser.parse_args()

    # Inicializa banco caso não exista
    init_db()

    if args.command == "start":
        start_session(args.project)
    elif args.command == "stop":
        stop_session(args.project)
    elif args.command == "report":
        report_sessions()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
