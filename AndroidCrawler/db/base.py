# coding: utf-8

import datetime
from sqlalchemy import Column, VARCHAR, TEXT, INTEGER, BINARY, TIMESTAMP, SMALLINT, BIGINT, FLOAT
from sqlalchemy.ext.declarative import declarative_base

__Base = declarative_base()


class DisCrawlerTasks(__Base):
    """class for mysql db table DisCrawlerTasks """
    __tablename__ = 'DisCrawlerTasks'
    submitter = Column('submitter', VARCHAR(128), nullable=True, default=None, index=True)
    url = Column('url', TEXT, nullable=False, default=None)
    header = Column('header', TEXT, nullable=True, default=None)
    priority = Column('priority', INTEGER, nullable=True, default=4)
    app_sha1 = Column('app_sha1', BINARY(20), nullable=True, default=None, index=True)
    status = Column('status', INTEGER, nullable=True, default=0)
    submit_time = Column('submit_time', TIMESTAMP, nullable=False,
                         default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    create_time = Column('create_time', TIMESTAMP, nullable=True, default=None, index=True)
    status_code = Column('status_code', INTEGER, nullable=True, default=0)
    market_table = Column('table_name', VARCHAR(20), nullable=True, default=None)
    id = Column('id', BIGINT, nullable=True, default=None)
    job_id = Column('job_id', BIGINT, nullable=False, autoincrement=True, primary_key=True)
    uniqueApk = Column('UniqueApk', SMALLINT, nullable=True, default=0)
    dealTag = Column('dealTag', SMALLINT, nullable=True, default=0)
    download_flag = Column('download_flag', INTEGER, nullable=True, default=0)
    mac_address = Column('mac_address', VARCHAR(128), nullable=True, default=None, index=True)
    download_count = Column('download_count', INTEGER, nullable=False, default=0, index=True)
    upload_flag = Column('upload_flag', INTEGER, nullable=True, default=0)
    sha256 = Column('Sha256', BINARY(32), nullable=True, default=None, index=True)

class IPProxyPool(__Base):
    """class for mysql db table IPProxyPool """
    __tablename__ = 'IPProxyPool'
    id = Column('id', BIGINT, nullable=False, autoincrement=True, primary_key=True)
    ip = Column('ip', VARCHAR(25), nullable=False)
    port = Column('port', INTEGER, nullable=False)
    validator = Column('validator', VARCHAR(64), nullable=True)
    country = Column('country', TEXT, nullable=True, default=None)
    anonymity = Column('anonymity', SMALLINT, nullable=True, default=None)
    https = Column('https', VARCHAR(4), nullable=True, default=None)
    speed = Column('speed', FLOAT, nullable=True, default=None)
    source = Column('source', VARCHAR(20), nullable=True, default=None)
    save_time = Column('save_time', TIMESTAMP, nullable=False,
                       default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    vali_count = Column('vali_count', INTEGER, nullable=True, default=3)



