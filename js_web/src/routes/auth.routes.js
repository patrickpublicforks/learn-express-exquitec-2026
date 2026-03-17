import  express from "express";
import * as controller from "../controller/auth.controller.js"
import { authMiddleware } from "../middlewares/auth.middleware.js";

const router = express.Router();

router.post("/login", controller.loginController)

router.post("/signup", controller.signupController);

router.get("/user", authMiddleware ,controller.profileController);

router.post("/test", controller.testRedis);

export default router