#! /usr/bin/env python
# encoding: utf-8

import os

# Necessary since we override different Contexts
import waflib.extras.wurftools as wt

def options(opt):
    opt.load('wurftools')

def configure(conf):

    conf.load('wurftools')

    if conf.env.TOOLCHAIN == 'linux':
        conf.check_cxx(lib = 'pthread')

    if conf.env['TOOLCHAIN'] == 'android':
	    conf.env.DEFINES += ['GTEST_OS_LINUX_ANDROID=1']


def build(bld):

    use_flags = []

    if bld.env.TOOLCHAIN == 'linux':

        ext_paths = ['/usr/lib/i386-linux-gnu', '/usr/lib/x86_64-linux-gnu']

        bld.read_shlib('pthread', paths = ext_paths)
        use_flags += ['pthread']

    bld.stlib(features = 'cxx',
	      source   = ['gtest/src/gtest-all.cc'],
	      target   = 'gtest',
              cxxflags = bld.toolchain_cxx_flags(),
	      includes = ['gtest/include',
                          'gtest'],
              export_includes = ['gtest/include'],
              use = use_flags)



