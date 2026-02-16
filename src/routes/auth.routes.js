import  express from "express";
import * as controller from "../controller/auth.controller.js"

const router = express.Router();

router.post("/login", controller.loginController)

router.post("/signup", controller.signupController);

export default router