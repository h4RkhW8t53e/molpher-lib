%module(directors="1") core
%feature("director") TreeOperation;
%feature("director") TraverseCallback;
%include "stl.i"

%{
#define SWIG_FILE_WITH_INIT
#include "morphing_functions.hpp"
#include "extensions/SAScore.h"
%}

//%init %{
//    SAScore::loadData();
//%}
%include "../../../backend/extensions/SAScore.h"

// complete morphing function
%include "include/morphing_functions.hpp";

// the molpher API
%include "include/molpher_API/molpher_API.i";