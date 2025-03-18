<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced HTML5 Elements and Forms</title>
</head>
<body>
    <!-- Ordered List with Roman Numerals -->
    <h2>Topics Covered</h2>
    <ol type="I">
        <li>HTML5 Elements</li>
        <li>HTML5 Forms</li>
        <li>Validation Attributes</li>
        <li>Multimedia Elements</li>
        <li>Semantic HTML</li>
    </ol>

    <!-- External Image from Pexels -->
    <h2>Image from Pexels - Instrucor said Pexels has no copyright issues</h2>
    <img src="https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg" 
         alt="Beautiful Landscape" width="400">

    <!-- Contact Table -->
    <h2>Contact List</h2>
    <table border="1" cellpadding="10" cellspacing="0">
        <thead>
            <tr>
                <th>Name</th>
                <th>Address</th>
                <th>Mobile</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John waswa</td>
                <td>123 Kakamega</td>
                <td>+254 712345678</td>
                <td>john.waswa@gmail.com</td>
            </tr>
            <tr>
                <td>Jane nasimiyu</td>
                <td>456 Kitale</td>
                <td>+254 798765432</td>
                <td>jane.nasimiyu@gmail.com</td>
            </tr>
            <tr>
                <td>Taylor Mbaya</td>
                <td>789 Bungoma</td>
                <td>+254 710987654</td>
                <td>taylor.mbaya@gmail.com</td>
            </tr>
            <tr>
                <td>Lisa Were</td>
                <td>101 Mumias</td>
                <td>+254 701234567</td>
                <td>lisa.were@gmail.com</td>
            </tr>
            <tr>
                <td>Peter Keter</td>
                <td>202 Kapsabet</td>
                <td>+254 789456123</td>
                <td>peter.keter@gmail.com</td>
            </tr>
        </tbody>
    </table>

    <!-- Registration Form -->
    <h2>Registration Form</h2>
    <form action="/submit" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required><br><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" placeholder="Enter your password" required><br><br>

        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" required><br><br>

        <!-- Dropdown -->
        <label for="role">Select Role:</label>
        <select id="role" name="role" required>
            <option value="">--Select--</option>
            <option value="student">Student</option>
            <option value="teacher">Teacher</option>
            <option value="admin">Admin</option>
        </select><br><br>

        <!-- Radio Buttons -->
        <label>Gender:</label>
        <input type="radio" id="male" name="gender" value="male" required> Male
        <input type="radio" id="female" name="gender" value="female" required> Female<br><br>

        <!-- Checkboxes -->
        <label>Interests:</label><br>
        <input type="checkbox" id="coding" name="interest" value="coding"> Coding<br>
        <input type="checkbox" id="sports" name="interest" value="sports"> Sports<br>
        <input type="checkbox" id="music" name="interest" value="music"> Music<br><br>

        <button type="submit">Submit</button>
        <button type="reset">Reset</button>
    </form>
</body>
</html>
