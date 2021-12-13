const http = require('http');

const server = http.createServer((req, res)=>{
    res.writeHead(200, {
        'Content-Type': 'text/html'
    }).end(`
        <h2>${ req.url }</h2>
    `);
});

server.listen(3000);
