import flet as ft
import threading
import sys

def main(page: ft.Page):
    page.title = "ПОБЕДА!"
    page.padding = 30
    page.bgcolor = "#FFF8E1"  # Светло-желтый фон
    
    # Функция для звука победы
    def play_victory_sound():
        try:
            # Для Windows
            import winsound
            winsound.Beep(1000, 500)
        except:
            # Универсальный системный звук
            print("\a")  # Простой бип в консоли
    
    # Обработчик кнопки
    def button_clicked(e):
        # Показать простое текстовое уведомление
        notification = ft.Text(
            value="УРА! Мы создали рабочую программу!",
            size=20,
            weight="bold",
            color="green"
        )
        page.add(notification)
        
        # Воспроизвести звук
        threading.Thread(target=play_victory_sound).start()
        
        # Обновить страницу
        page.update()
    
    # Создаем кнопку с минимальными зависимостями
    victory_button = ft.ElevatedButton(
        text="НАЖМИ МЕНЯ!",
        width=300,
        height=100,
        bgcolor="#388E3C",  # Зеленый
        color="white",      # Белый текст
        on_click=button_clicked
    )
    
    # Собираем интерфейс
    page.add(
        ft.Text(
            value="ПОБЕДНОЕ ПРИЛОЖЕНИЕ",
            size=28,
            weight="bold",
            color="#5D4037"  # Коричневый
        ),
        victory_button,
        ft.Text(
            value="Нажмите кнопку, чтобы услышать звук победы!",
            size=16,
            italic=True,
            color="gray"
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
