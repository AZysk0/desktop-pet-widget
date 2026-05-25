import os
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QHBoxLayout
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QMovie


class SetupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Pet Setup")
        self.setFixedSize(400, 150)
        
        self.selected_path = None

        # Layout UI
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        
        self.status_label = QLabel("No GIF selected. Using default fallback if available.", self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.status_label)

        # Buttons layout
        self.btn_layout = QHBoxLayout()
        
        self.select_btn = QPushButton("Browse GIF...", self)
        self.select_btn.clicked.connect(self.browse_file)
        self.btn_layout.addWidget(self.select_btn)
        
        self.launch_btn = QPushButton("Launch Pet", self)
        self.launch_btn.clicked.connect(self.accept_and_close)
        self.btn_layout.addWidget(self.launch_btn)
        
        self.layout.addLayout(self.btn_layout)
        self.setCentralWidget(self.central_widget)

    def browse_file(self):
        # Open native OS file dialog filtering for GIFs
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Pet Animation", "", "GIF Images (*.gif)"
        )
        if file_path:
            self.selected_path = file_path
            # Just show the filename on screen, not the long messy path
            self.status_label.setText(f"Selected: {os.path.basename(file_path)}")

    def accept_and_close(self):
        # Close this configuration window so the main loop can continue
        self.close()




