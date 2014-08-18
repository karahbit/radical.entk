#!/usr/bin/env python

"""This module defines and implements the Task class.
"""

__author__    = "Ole Weider <ole.weidner@rutgers.edu>"
__copyright__ = "Copyright 2014, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.ensemblemd.file import File

# ------------------------------------------------------------------------------
#
class Task(object):

    #---------------------------------------------------------------------------
    #
    def __init__(self):
        """ Creates a new Task object.
        """
        self._kernel = None
        self._expected_output = list()
        self._requires_input = dict()

    #---------------------------------------------------------------------------
    #
    def size(self):
        """ Returns the size. If called for a Task, size() returns always '1'. 
            If called for a Batch, size() returns the number of tasks in the 
            Batch.
        """
        return 1

    #---------------------------------------------------------------------------
    #
    def set_kernel(self, kernel):
        """Sets the application kernel that gets executed in this Subtask.
        """
        self._kernel = kernel

    #---------------------------------------------------------------------------
    #
    def add_output(self, filename):
        """Asserts the existence of a specific file after the step has completed.
        """
        self._expected_output.append(filename)
        return File()
        
    #---------------------------------------------------------------------------
    #
    def assert_output(self, filename):
        """Asserts the existence of a specific file after the step has completed.
        """

    #---------------------------------------------------------------------------
    #
    def add_input(self, dataobject, label):
        """TODO: document me
        """
        self._requires_input[label] = "full_path_to_file"

    #---------------------------------------------------------------------------
    #
    def _get_task_description(self):
        """Returns the task description.
        """
        description = {
            "kernel"          : self._kernel._get_kernel_description(),
            "requires_input"  : self._requires_input,
            "expected_output" : self._expected_output 
        }

        return description
