const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res)=>{
    console.log('---a');
    fs.writeFile(
        __dirname + '/headers01.txt',
        JSON.stringify(req.headers),
        (error)=>{
            if(!error){
                console.log('---b');
                res.end('ok');
            } else {
                console.log('---c');
                res.end(error);
            }
        });
    console.log('---d');
});

server.listen(3000);
