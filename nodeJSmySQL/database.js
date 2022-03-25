const {createPool} = require('mysql')

const pool = createPool({
  host:"localhost",
  user:"root",
  password:"00365633",
  connectionLimit: 10
})

pool.query(`select * from twitchchat.users`,(err,res)=>{
  return console.log(res)
})