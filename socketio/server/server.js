const express = require("express");
const app = express();
const cors = require("cors");
// create instance of http library
const http  = require("http");
const {Server} = require("socket.io");
app.use(cors());
const server = http.createServer(app);

const io = new Server(server,{cors :{
    origin:"http://localhost:3000",
    methods:["GET", "POST"]
}});

io.on("connection", (socket)=>{
    console.log(`user connected ${socket.id}`);
    socket.on("feedback", (data)=>{
        // console.log(data);
        socket.broadcast.emit("receive_feedback", data)
    })
})
server.listen(8000, ()=>{
    console.log(" >> Server is running on port 8000 << ");
})