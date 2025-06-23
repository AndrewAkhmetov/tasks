class Report:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class PDFGenerator:
    @staticmethod
    def generate_from_report(report: Report) -> str:
        return f'Репорт {report.title} с {report.content} сохранен в PDF'


class FileSave:
    @staticmethod
    def save_report(report: Report) -> str:
        return f'Репорт {report.title} с {report.content} сохранен в файл'
