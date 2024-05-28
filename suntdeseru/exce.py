   from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget

   class MyMainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           self.setWindowTitle("My App")

           # Create a vertical layout
           layout = QVBoxLayout()

           # Add a widget (e.g., Color widget) to the layout
           layout.addWidget(Color('red'))  # Replace 'Color' with your actual widget

           # Create a central widget and set the layout
           widget = QWidget()
           widget.setLayout(layout)
           self.setCentralWidget(widget)
   