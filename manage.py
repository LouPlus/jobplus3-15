#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jobplus.app import create_app

app = create_app('development')


if __name__ == '__main__':
    app.run()
