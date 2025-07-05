import flet as ft

def main(page: ft.Page):
    page.title = "My App"
    page.add(ft.Text("Hello World!"))

if __name__ == "__main__":
    ft.app(target=main)
