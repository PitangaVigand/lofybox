from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QTimer, Qt
from src.spotify_controller import start_or_resume_playlist, stop_playback


class LofyBoxWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lofybox")
        self.setFixedSize(300, 400)

        self.total_seconds = 25 * 60
        self.remaining_seconds = self.total_seconds

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Tempo
        self.timer_label = QLabel(self.format_time(self.remaining_seconds))
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 48px;")

        # Subtítulo
        self.subtitle = QLabel("Next Up: Focus")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setStyleSheet("color: gray; font-size: 14px;")

        # Botão de play/pause
        self.play_button = QPushButton("▶️")
        self.play_button.setFixedSize(60, 60)
        self.play_button.setStyleSheet("font-size: 24px; border-radius: 30px;")
        self.play_button.clicked.connect(self.toggle_timer)

        # Layout botão
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.play_button)
        button_layout.addStretch()

        # Monta a interface
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.subtitle)
        self.layout.addSpacing(20)
        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)

        self.is_running = False

    def toggle_timer(self):
        if self.is_running:
            self.timer.stop()
            self.play_button.setText("▶️")
            stop_playback()
        else:
            self.timer.start()
            self.play_button.setText("⏸️")
            start_or_resume_playlist()
        self.is_running = not self.is_running

    def update_timer(self):
        self.remaining_seconds -= 1
        if self.remaining_seconds <= 0:
            self.timer.stop()
            self.play_button.setText("✅")
        self.timer_label.setText(self.format_time(self.remaining_seconds))

    def format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"
