import { sequelize } from "../config/db.config.js"
export *  from "./user/User.js"

(async () => {
    await sequelize.sync()
})()