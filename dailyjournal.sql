CREATE TABLE `tags` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tag` TEXT NOT NULL
);

CREATE TABLE `moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood` TEXT NOT NULL
);


CREATE TABLE `entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date` DATE NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id` INTEGER,
    FOREIGN KEY(`mood_id`) REFERENCES `moods`(`id`)
);

CREATE TABLE `entrytags` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tag_id` INTEGER,
    `entry_id` INTEGER,
    FOREIGN KEY(`entry_id`) REFERENCES `entries`(`id`)
    FOREIGN KEY(`tag_id`) REFERENCES `tags`(`id`)
);

INSERT INTO `tags` VALUES (null, "API");

INSERT INTO `moods` VALUES (null, "surprised");
INSERT INTO `moods` VALUES (null, "mad");
INSERT INTO `moods` VALUES (null, "sad");
INSERT INTO `moods` VALUES (null, "happy");
INSERT INTO `moods` VALUES (null, "anxious");

INSERT INTO `entries` VALUES (null, "2020-07-07", "Today we learned about storing data in an API", 4);

INSERT INTO `entrytags` VALUES (null, 1, 1);

SELECT * FROM entries