const http = require('http');
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

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');

    const database = process.argv[2];

    countStudents(database)
      .then((data) => {
        res.end(data);
      })
      .catch((error) => {
        res.end(error.message);
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
