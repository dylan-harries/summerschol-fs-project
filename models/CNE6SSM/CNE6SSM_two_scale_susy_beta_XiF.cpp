// ====================================================================
// This file is part of FlexibleSUSY.
//
// FlexibleSUSY is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published
// by the Free Software Foundation, either version 3 of the License,
// or (at your option) any later version.
//
// FlexibleSUSY is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with FlexibleSUSY.  If not, see
// <http://www.gnu.org/licenses/>.
// ====================================================================

// File generated at Thu 22 Jan 2015 11:47:09

#include "CNE6SSM_two_scale_susy_parameters.hpp"
#include "wrappers.hpp"

namespace flexiblesusy {

#define INPUT(parameter) input.parameter
#define TRACE_STRUCT susy_traces

/**
 * Calculates the one-loop beta function of XiF.
 *
 * @return one-loop beta function
 */
double CNE6SSM_susy_parameters::calc_beta_XiF_one_loop(const Susy_traces& susy_traces) const
{


   double beta_XiF;

   beta_XiF = oneOver16PiSqr*(2*AbsSqr(KappaPr) + AbsSqr(Sigmax) + 2*
      AbsSqr(SigmaL))*XiF;


   return beta_XiF;
}

/**
 * Calculates the two-loop beta function of XiF.
 *
 * @return two-loop beta function
 */
double CNE6SSM_susy_parameters::calc_beta_XiF_two_loop(const Susy_traces& susy_traces) const
{
   const auto QS = INPUT(QS);
   const double tracegDAdjgD = TRACE_STRUCT.tracegDAdjgD;
   const double tracehEAdjhE = TRACE_STRUCT.tracehEAdjhE;
   const double traceKappaAdjKappa = TRACE_STRUCT.traceKappaAdjKappa;
   const double traceLambda12AdjLambda12 =
      TRACE_STRUCT.traceLambda12AdjLambda12;


   double beta_XiF;

   beta_XiF = -0.1*twoLoop*XiF*(40*AbsSqr(KappaPr)*(AbsSqr(Sigmax) + 2*
      AbsSqr(SigmaL)) + 4*AbsSqr(SigmaL)*(15*tracegDAdjgD + 5*tracehEAdjhE + 10
      *AbsSqr(SigmaL) - 3*Sqr(g1) - 2*Sqr(g1p) - 15*Sqr(g2)) + AbsSqr(Sigmax)*(
      30*traceKappaAdjKappa + 20*traceLambda12AdjLambda12 + 20*AbsSqr(Lambdax)
      - Sqr(g1p)*Sqr(QS)) + 80*Sqr(Conj(KappaPr))*Sqr(KappaPr) + 20*Sqr(Conj(
      Sigmax))*Sqr(Sigmax));


   return beta_XiF;
}

} // namespace flexiblesusy
