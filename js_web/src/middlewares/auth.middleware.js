import { verifyJwtToken } from "../config/jwt.config.js"

export function authMiddleware(req, res, next){
    try {
      const raw_token = req.headers["authorization"];
      let token = raw_token.split(" ")[1];
      let claim = verifyJwtToken(token);
      req.user_id = claim.user_id;
      next()
    } catch(err) {
        return res.status(401).json({
            message: "unauthorized"
        })
    }

    
}