const express = require('express')
const app = express();
const path = require('path');
const multer = require('multer');
const { exec } = require('child_process');
var shell = require('shelljs');
const utf8 = require('utf8');
var fs = require('fs');
var response = "";
var filename = "";
var uploadspath = "/home/elwess/Desktop/nodeVision/public/uploads/";
var pythonPath = "/home/elwess/Desktop/nodeVision/python-ocr-example-master/";
const storage = multer.diskStorage({
    destination: './public/uploads/',
    filename: function (req, file, cb) {
        cb(null, file.fieldname + '' + Date.now() + path.extname(file.originalname));
        filename = file.fieldname + '' + Date.now() + path.extname(file.originalname);
    }
});

app.use(express.static('./public'));

const upload = multer({
    storage: storage
}).single('myImage')

app.get('/', (req, res) => {
    res.send('Hello World!')
});
app.post('/upload', (req, res) => {
    upload(req, res, (err) => {
        if (err) {
            console.log(err);
        } else {
            var myfilename = filename;
            
            shell.cd(pythonPath);
            var resp = shell.exec('python ocr_script.py ' + uploadspath+req.file.filename);
            shell.exec('python face_detection.py ' +uploadspath+req.file.filename);
            console.log(uploadspath + 'face' + filename+"----------------------------")
            var imageAsBase64 = fs.readFileSync(uploadspath + 'face' + req.file.filename, 'base64');

            res.status(200).send({'text':resp, 'img': imageAsBase64});
        }
    });
});
app.listen(8000, () => {
    console.log('Example app listening on port 8000!')
});
