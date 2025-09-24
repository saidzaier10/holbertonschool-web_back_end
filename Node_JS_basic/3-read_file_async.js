const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Read the file asynchronously
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split into lines and filter out empty lines
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Remove the header line
      const students = lines.slice(1);

      // Initialize storage for fields
      const fields = {};
      let totalStudents = 0;

      // Process each student
      students.forEach((student) => {
        const studentData = student.split(',');
        // Check if it's a valid student line (has all fields)
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

      // Display results
      console.log(`Number of students: ${totalStudents}`);

      // Display per field
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const list = fields[field];
          console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        }
      }

      resolve();
    });
  });
}

module.exports = countStudents;
