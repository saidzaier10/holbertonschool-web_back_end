const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      let totalStudents = 0;

      students.forEach((student) => {
        const studentData = student.split(',');
        if (studentData.length === 4 && studentData[0]) {
          const firstname = studentData[0];
          const field = studentData[3];

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
          totalStudents += 1;
        }
      });

      let output = `Number of students: ${totalStudents}\n`;

      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const list = fields[field];
          output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
        }
      }

      resolve(output.trim());
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  const database = process.argv[2];

  let responseText = 'This is the list of our students\n';

  countStudents(database)
    .then((data) => {
      responseText += data;
      res.send(responseText);
    })
    .catch((error) => {
      responseText += error.message;
      res.send(responseText);
    });
});

app.listen(1245);

module.exports = app;
