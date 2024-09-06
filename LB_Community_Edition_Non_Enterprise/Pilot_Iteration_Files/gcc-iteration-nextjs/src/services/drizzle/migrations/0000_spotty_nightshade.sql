CREATE TABLE `attendees`
(
    `id`         text PRIMARY KEY               NOT NULL,
    `created_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
    `email`      text                           NOT NULL,
    `name`       text                           NOT NULL
);
--> statement-breakpoint
CREATE TABLE `events`
(
    `id`           text PRIMARY KEY                  NOT NULL,
    `created_at`   text    DEFAULT CURRENT_TIMESTAMP NOT NULL,
    `name`         text                              NOT NULL,
    `startOn`      text                              NOT NULL,
    `createdById`  text                              NOT NULL,
    `description`  text,
    `streetNumber` integer,
    `street`       text,
    `zip`          integer,
    `bldg`         text,
    `isPrivate`    integer DEFAULT false             NOT NULL,
    `status`       text    DEFAULT 'draft'           NOT NULL
);
--> statement-breakpoint
CREATE TABLE `rsvps`
(
    `id`         text PRIMARY KEY               NOT NULL,
    `created_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
    `attendeeId` text,
    `eventId`    text,
    `status`     text DEFAULT 'going'           NOT NULL
);
--> statement-breakpoint
CREATE TABLE `users`
(
    `id`         text PRIMARY KEY               NOT NULL,
    `created_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
    `email`      text                           NOT NULL,
    `password`   text                           NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `attendees_email_unique` ON `attendees` (`email`);--> statement-breakpoint
CREATE UNIQUE INDEX `events_createdById_name_unique` ON `events` (`createdById`, `name`);--> statement-breakpoint
CREATE UNIQUE INDEX `rsvps_attendeeId_eventId_unique` ON `rsvps` (`attendeeId`, `eventId`);--> statement-breakpoint
CREATE UNIQUE INDEX `users_email_unique` ON `users` (`email`);