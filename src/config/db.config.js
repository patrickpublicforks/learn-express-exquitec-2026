// database.js
import { Sequelize } from 'sequelize';

// Option 2: Passing parameters separately (sqlite)
export const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './database.sqlite', // or ':memory:' for in-memory
});


async function testConnection() {
  try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }
}

testConnection();
