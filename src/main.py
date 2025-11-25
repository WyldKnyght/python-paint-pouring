"""Main entry point for the paint pouring simulator."""

import sys
import pygame
from src.config import config
from src.ui.main_window import PaintPouringWindow


def main() -> int:
    """Initialize and run the application.
    
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    try:
        # Initialize Pygame
        pygame.init()
        
        # Create and run main window
        window = PaintPouringWindow(config)
        window.run()
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    finally:
        pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
