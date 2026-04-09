CREATE TABLE docker_learning (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(100),
    learned_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO docker_learning (topic) VALUES ('PostgreSQL in Docker'), ('Port mapping');