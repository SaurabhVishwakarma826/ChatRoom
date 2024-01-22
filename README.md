# Flask Chat Application

This is a simple chat application built using Flask, MongoDB, and Socket.IO. Users can create rooms, invite others to join, and exchange real-time messages within those rooms.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (login, signup, logout)
- Create and edit chat rooms
- Real-time messaging using Socket.IO
- View room members and past messages
- MongoDB for data storage

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SaurabhVishwakarma826/ChatRoom.git
    cd ChatRoom
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up MongoDB:**
    - Create a MongoDB database and update the connection details in `db.py`.

4. **Run the application:**

    ```bash
    python your_app_name.py
    ```

5. **Access the application:**
    - Visit `http://localhost:5000` in your web browser.

## Usage

- Visit the homepage (`/`) to see available chat rooms.
- Log in or sign up to access additional features.
- Create new chat rooms or join existing ones.
- Exchange real-time messages within the chat rooms.
- Edit room details, including room name and members.

## Screenshots

Include screenshots or GIFs showcasing the main features of your application.

## Technologies Used

- Flask
- MongoDB
- Socket.IO
- HTML/CSS
- JavaScript

## Contributing

Feel free to contribute to this project. To contribute, follow these steps:

1. **Fork the repository**
2. **Create a new branch for your feature:**
    ```bash
    git checkout -b feature-name
    ```
3. **Commit your changes:**
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature-name
    ```
5. **Submit a pull request**

---

Happy coding! If you have any questions or issues, feel free to open an [issue](https://github.com/SaurabhVishwakarma826/ChatRoom/issues).
