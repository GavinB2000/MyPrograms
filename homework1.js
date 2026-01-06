const http = require('http')

const server = http.createServer((req,res)=> {
    console.log('The request header is:');
    console.log(req.headers);
    let ff = 0;
    if (req.headers['user-agent'].includes("Firefox")) {
        ff ++;
        res.end('User Agent: Firefox' + "\n number of requests " + ff);
    } else if (req.headers['user-agent'].includes("Chrome")) {
        res.end('User Agent: Chrome');
    } else if (req.headers['user-agent'].includes("Safari")) {
        res.end('User Agent: Safari')
    } else if (req.headers['user-agent'].includes("Curl")) {
        res.end('User Agent: curl')
    } else {
        res.end('User Agent: Unkown agent');
    }
});

server.listen(3000, function() {
    console.log("Server running on 3000");
});
// control + C stops the server
// curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0" http://localhost:3000
// curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.6 Safari/537.36" http://localhost:3000
// curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36" http://localhost:3000
// curl http://localhost:3000
// curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko" http://localhost:3000
// res.end(`User Agent: agentName\nNo of Requests received = ${agentCount}`);