#!/usr/bin/env python

from dineviz.app import app

print 'Server Starting'
app.run(debug=True, host='0.0.0.0')

