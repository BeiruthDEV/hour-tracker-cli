import argparse
from tracker import storage, core


def main():
    parser = argparse.ArgumentParser(description="HourTracker - Controle de horas em projetos")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Start
    start_parser = subparsers.add_parser("start", help="Inicia contagem de horas em um projeto")
    start_parser.add_argument("project", type=str, help="Nome do projeto")

    # Stop
    stop_parser = subparsers.add_parser("stop", help="Finaliza contagem de horas em um projeto")
    stop_parser.add_argument("project", type=str, help="Nome do projeto")

    # Report
    subparsers.add_parser("report", help="Gera relatório de horas acumuladas")

    args = parser.parse_args()
    storage.init_db()

    if args.command == "start":
        core.start_project(args.project)
        print(f"Início registrado para o projeto '{args.project}'.")

    elif args.command == "stop":
        core.stop_project(args.project)
        print(f"Fim registrado para o projeto '{args.project}'.")

    elif args.command == "report":
        report = core.generate_report()
        print("Horas acumuladas por projeto:")
        for project, hours in report.items():
            print(f" - {project}: {hours:.2f}h")


if __name__ == "__main__":
    main()
