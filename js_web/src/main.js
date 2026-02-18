import dotenv from "dotenv"; dotenv.config();
import  express from "express";
import cors from "cors"
import morgan from "morgan";

import authRouter from "./routes/auth.routes.js"

const app =  express()

app.use(cors())
morgan.token('body', (req) => JSON.stringify(req.body || {}));
app.use(express.json())

app.use(
  morgan((tokens, req, res) => {
    return JSON.stringify({
      method: tokens.method(req, res),
      url: tokens.url(req, res),
      status: Number(tokens.status(req, res)),
      content_length: tokens.res(req, res, 'content-length'),
      response_time_ms: Number(tokens['response-time'](req, res)),
      body: req.method !== 'GET' ? tokens.body(req, res) : undefined,
      response: res.res_body ?? {},
      timestamp: new Date().toISOString(),
    });
  })
);
app.use((req, res, next) => {
    try {
        const json = res.json.bind(res);
        res.json  = (body) =>{
            res.res_body = body;
            json(body)
        }
        next()
    } catch (error){
        next(error)
    }
})

app.use('/', authRouter)


app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error stack for debugging
  res.status(err.status || 500).json({
    status: "error",
    message: err.message || "I caught you",
  });
});


export default app