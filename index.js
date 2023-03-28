var express = require("express")
var bodyParser = require('body-parser');  
const cors = require('cors')

app=express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))
app.use(cors())
fs =require('fs')


var data = {
  "Led":0,
}
fs.writeFileSync(__dirname+'/data.json', JSON.stringify(data))

app.get("/", (req,res)=>{
  res.json(data)
})
app.post("/", (req,res)=>{
  data=req.body
  fs.writeFileSync(__dirname+'/data.json', JSON.stringify(data))
  //if not used status 0
  res.json({"status":0}).status(200)
  //if used send status 1
})

//state of the robot
var databack = require('./databack.json');
app.get("/botState", (req,res) => {
  if(databack["botstate"]== true){
    res.json({botState: "Available"});
  }
  if(databack["botstate"]== false){
    res.json({botState: "Busy"});
  }
});
//state of the battery
app.get("/batteryState", (req,res) => {
    res.json({batteryState: databack["batterystate"]});
});

app.listen(8000,'0.0.0.0', () => {
  console.log("server starting on port : 8000" )
});
