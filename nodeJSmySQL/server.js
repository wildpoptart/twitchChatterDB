const express = require("express")
const cors = require("cors")
const app = express();
var cors0ptions = {
    origin: "localhost"
};
app.use(cors(cors0ptions));
app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.get("/", (req,res) => {
    res.json({message: "Welcome to wildpoptart app"});
});

// set port, listen for requests
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});