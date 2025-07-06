import flet as ft
import threading
import os
import sys
import urllib.request

def main(page: ft.Page):
    page.title = "ПОБЕДА!"
    page.bgcolor = "#FFF8E1"
    
    # Центрируем содержимое по вертикали и горизонтали
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    
    # Проверяем и скачиваем звуковой файл
    sound_file = "victory.mp3"
    if not os.path.exists(sound_file):
        try:
            urllib.request.urlretrieve(
                "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3",
                sound_file
            )
        except:
            sound_file = None
    
    # Создаем аудио элемент для воспроизведения внутри приложения
    audio = ft.Audio(
        src=sound_file or "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3",
        autoplay=False,
        volume=1.0,
        balance=0.0,
    )
    page.overlay.append(audio)
    
    # Функция для звука победы
    def play_victory_sound():
        if audio.src:
            audio.play()
        else:
            # Резервный вариант: системный звук
            print("\a")  # Простой бип в консоли
    
    # Обработчик кнопки
    def button_clicked(e):
        # Показать уведомление
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
    
    # Создаем кнопку
    victory_button = ft.ElevatedButton(
        text="НАЖМИ МЕНЯ!",
        width=300,
        height=100,
        bgcolor="#388E3C",
        color="white",
        on_click=button_clicked
    )
    
    # Создаем контейнер с центрированным содержимым
    content = ft.Column(
        [
            ft.Text(
                value="ПОБЕДНОЕ ПРИЛОЖЕНИЕ",
                size=28,
                weight="bold",
                color="#5D4037",
                text_align=ft.TextAlign.CENTER
            ),
            ft.Divider(height=40, color="transparent"),
            victory_button,
            ft.Divider(height=40, color="transparent"),
            ft.Text(
                value="Нажмите кнопку, чтобы услышать звук победы!",
                size=16,
                italic=True,
                color="gray",
                text_align=ft.TextAlign.CENTER
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
    
    # Добавляем контейнер с безопасными отступами
    container = ft.Container(
        content=content,
        padding=ft.padding.symmetric(horizontal=20, vertical=40),
        expand=True
    )
    
    # Добавляем основной контейнер на страницу
    page.add(container)

if __name__ == "__main__":
    # Запускаем в нативном окне (не в браузере)
    ft.app(target=main)
