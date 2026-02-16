// models/User.js
import { DataTypes } from 'sequelize';
import { sequelize }  from '../../config/db.config.js';

export const User = sequelize.define(
  "User",
  {
    // Model attributes are defined here
    username: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
    password: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    age: {
      type: DataTypes.INTEGER,
      allowNull: true,
    },
  },
  {
    // Other model options go here
  },
);


