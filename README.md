# 🎓 Student Management System

A full-featured web application to add students,add teacher,manage student,manage teacher and attendance efficiently.

![GitHub repo size](https://img.shields.io/github/repo-size/shahsilashafee121/student-management-system?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/shahsilashafee121/student-management-system?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/shahsilashafee121/student-management-system?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---



---

## ✨ Features

- 👨‍🎓 **Student Registration** — Add, edit, and delete student records
- 📚 **Course Management** — Manage courses and subject assignments
- 📅 **Attendance Tracking** — Mark and monitor daily attendance
- 🔐 **Authentication** — Secure login for admin and teachers
- 📊 **Dashboard** — Overview of students, courses, and performance
- 🔍 **Search & Filter** — Quickly find students by name or ID

---

## 🛠️ Built With

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white)
---

## 📁 Project Structure

```
student-management-system/
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   └── App.js
├── server/                 # Express backend
│   ├── models/             # MongoDB models
│   ├── routes/             # API routes
│   ├── controllers/        # Business logic
│   └── server.js
├── .env.example
├── package.json
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/shahsilashafee121/student-management-system.git
cd student-management-system
```

### 2. Install dependencies
```bash
# Install server dependencies
cd server
npm install

# Install client dependencies
cd ../client
npm install
```

### 3. Configure environment variables
```bash
# In /server create a .env file
cp .env.example .env
```
Add the following to your `.env`:
```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
```

### 4. Run the application
```bash
# Run backend
cd server
npm run dev

# Run frontend (new terminal)
cd client
npm start
```

### 5. Open in browser
```
http://localhost:3000
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/students` | Get all students |
| POST | `/api/students` | Add new student |
| PUT | `/api/students/:id` | Update student |
| DELETE | `/api/students/:id` | Delete student |
| GET | `/api/courses` | Get all courses |
| POST | `/api/attendance` | Mark attendance |
| GET | `/api/grades/:id` | Get student grades |

---

## 👤 Default Login

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@school.com | admin123 |
| Teacher | teacher@school.com | teacher123 |

> ⚠️ Change these credentials after first login!

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📫 Contact

**Shahsila Shafeer**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shahsila-shafeer-960b07326)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yourname@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shahsilashafee121)

---

⭐ *If you found this project helpful, please give it a star!*
