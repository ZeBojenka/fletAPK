import flet as ft

def main(page: ft.Page):
    page.title = "GitHub APK Builder"
    page.add(
        ft.Text("Привет от Flet!", size=30),
        ft.ElevatedButton("Нажми меня", on_click=lambda e: print("Действие!"))
    )

ft.app(target=main)