import os
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QMenu
from PyQt6.QtCore import Qt, QPoint, QSize
from PyQt6.QtGui import QMovie, QAction


class TransparentOverlay(QMainWindow):
    def __init__(self, gif_path, scale_factor=1.0):
        super().__init__()
        
        # 1. Strip borders, pin to top, and hide from taskbar
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        
        # 2. Enable click-through alpha transparency
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        
        # Variable to keep track of mouse coordinates when dragging
        self.drag_position = QPoint()

        # 3. Layout layout configuration (Zero margins so the canvas fits tightly)
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.central_widget)

        # 4. GIF Display Container
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.gif_label)

        # 5. Initialize and scale the animation
        self.movie = QMovie(gif_path)
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        # Grab frame size to match window boundaries perfectly
        native_size = self.movie.currentImage().size()
        if native_size.isValid() and native_size.width() > 0:
            target_width = int(native_size.width() * scale_factor)
            target_height = int(native_size.height() * scale_factor)
            self.movie.setScaledSize(QSize(target_width, target_height))
            self.setGeometry(100, 100, target_width, target_height)
        else:
            self.setGeometry(100, 100, 300, 300) # Fallback dimension

    # --- Mouse Dragging Routing ---
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    # --- Right Click Menu to Close ---
    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        quit_action = QAction("Close pet", self)
        quit_action.triggered.connect(lambda: os._exit(0))
        context_menu.addAction(quit_action)
        context_menu.exec(event.globalPos())


