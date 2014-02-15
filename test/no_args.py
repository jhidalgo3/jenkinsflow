#!/usr/bin/python

# Copyright (c) 2012 - 2014 Lars Hupfeldt Nielsen, Hupfeldt IT
# All rights reserved. This work is under a BSD license, see LICENSE.TXT.

from __future__ import print_function

from jenkinsflow.jobcontrol import serial

from framework import mock_api

def main():
    with mock_api.api(job_name_prefix=__file__) as api:
        api.job('job-1', exec_time=0.5, max_fails=0, expect_invocations=1, expect_order=1)
        print()

        with serial(api, timeout=70, job_name_prefix=api.job_name_prefix, report_interval=1) as ctrl1:
            ctrl1.invoke('job-1')

if __name__ == '__main__':
    main()
