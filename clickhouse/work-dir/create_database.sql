-- Tạo database
DROP DATABASE IF EXISTS streaming_history;
CREATE DATABASE streaming_history;

-- Bảng dim_album
CREATE TABLE streaming_history.dim_album
(
    album_name String,
    album_id UInt64
)
ENGINE = MergeTree
ORDER BY album_id;

-- Bảng dim_artist
CREATE TABLE streaming_history.dim_artist
(
    artist_name String,
    artist_id UInt64
)
ENGINE = MergeTree
ORDER BY artist_id;

-- Bảng dim_track
CREATE TABLE streaming_history.dim_track
(
    spotify_track_uri String,
    track_name String,
    album_id UInt64,
    artist_id UInt64,
    track_id UInt64
)
ENGINE = MergeTree
ORDER BY track_id;

-- Bảng dim_platform
CREATE TABLE streaming_history.dim_platform
(
    platform String,
    platform_id UInt64
)
ENGINE = MergeTree
ORDER BY platform_id;

-- Bảng fact_stream
CREATE TABLE streaming_history.fact_stream
(
    ts DateTime,
    ms_played UInt64,
    skipped Boolean,
    offline Boolean,
    incognito_mode Boolean,
    reason_start String,
    reason_end String,
    shuffle Boolean,
    track_id UInt64,
    platform_id UInt64
)
ENGINE = MergeTree
ORDER BY (ts, track_id);