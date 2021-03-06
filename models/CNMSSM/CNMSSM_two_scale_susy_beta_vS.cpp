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

// File generated at Fri 9 Jan 2015 15:06:37

#include "CNMSSM_two_scale_susy_parameters.hpp"
#include "wrappers.hpp"

namespace flexiblesusy {

#define INPUT(parameter) input.parameter
#define TRACE_STRUCT susy_traces

/**
 * Calculates the one-loop beta function of vS.
 *
 * @return one-loop beta function
 */
double CNMSSM_susy_parameters::calc_beta_vS_one_loop(const Susy_traces& susy_traces) const
{


   double beta_vS;

   beta_vS = -2*oneOver16PiSqr*vS*(AbsSqr(Kappa) + AbsSqr(Lambdax));


   return beta_vS;
}

/**
 * Calculates the two-loop beta function of vS.
 *
 * @return two-loop beta function
 */
double CNMSSM_susy_parameters::calc_beta_vS_two_loop(const Susy_traces& susy_traces) const
{
   const double traceYdAdjYd = TRACE_STRUCT.traceYdAdjYd;
   const double traceYeAdjYe = TRACE_STRUCT.traceYeAdjYe;
   const double traceYuAdjYu = TRACE_STRUCT.traceYuAdjYu;


   double beta_vS;

   beta_vS = twoLoop*(8*vS*AbsSqr(Kappa)*AbsSqr(Lambdax) + 0.4*vS*AbsSqr(
      Lambdax)*(15*traceYdAdjYd + 5*traceYeAdjYe + 15*traceYuAdjYu + 10*AbsSqr(
      Lambdax) - 3*Sqr(g1) - 15*Sqr(g2)) + 8*vS*Sqr(Conj(Kappa))*Sqr(Kappa));


   return beta_vS;
}

} // namespace flexiblesusy
