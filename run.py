import sys
import os
from PyQt6.QtWidgets import QApplication

from app.views.setup import SetupWindow
from app.views.pet import TransparentOverlay


def main():
    app = QApplication(sys.argv)
    setup = SetupWindow()
    setup.show()
    app.exec()
    
    chosen_gif = setup.selected_path
    if not chosen_gif:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chosen_gif = os.path.join(current_dir, "assets", "character_idle.gif")
    
    if os.path.exists(chosen_gif):
        # Passing your chosen file and a 1.5x scale multiplier
        pet = TransparentOverlay(gif_path=chosen_gif, scale_factor=1)
        pet.show()
        
        # Start the second event loop to keep your pet animating on screen
        sys.exit(app.exec())
    else:
        print(f"Error: Could not find any valid GIF to display at:\n {chosen_gif}")

if __name__ == "__main__":
    main()
