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

// File generated at Thu 22 Jan 2015 11:54:07

#ifndef CNE6SSM_UTILITIES_H
#define CNE6SSM_UTILITIES_H

#include "CNE6SSM_two_scale_model.hpp"
#include "CNE6SSM_info.hpp"
#include "wrappers.hpp"

#include <Eigen/Core>
#include <string>
#include <vector>
#include <valarray>
#include <utility>

#define PHYSICAL(p) model.get_physical().p
#define MODELPARAMETER(p) model.get_##p()

namespace flexiblesusy {

class CNE6SSM_parameter_getter {
public:
   Eigen::ArrayXd get_parameters(const CNE6SSM<Two_scale>& model) {
      return model.get();
   }
   std::vector<std::string> get_parameter_names(const CNE6SSM<Two_scale>&) const {
      using namespace CNE6SSM_info;
      return std::vector<std::string>(parameter_names,
                                      parameter_names + NUMBER_OF_PARAMETERS);
   }
};

class CNE6SSM_spectrum_plotter {
public:
   CNE6SSM_spectrum_plotter();
   ~CNE6SSM_spectrum_plotter() {}

   template <class T>
   void extract_spectrum(const CNE6SSM<T>&);
   void write_to_file(const std::string&) const;

private:
   struct TParticle {
      std::string name;
      std::string latex_name;
      std::valarray<double> masses;
      TParticle(const std::string& name_, const std::string& latex_name_,
                const std::valarray<double>& masses_)
         : name(name_)
         , latex_name(latex_name_)
         , masses(masses_)
         {}
   };
   typedef std::vector<TParticle> TSpectrum;
   TSpectrum spectrum;
   double scale;
   unsigned width;

   void write_spectrum(const TSpectrum&, std::ofstream&) const;
   static std::valarray<double> to_valarray(double);
   template <class Scalar, int M, int N>
   static std::valarray<double> to_valarray(const Eigen::Array<Scalar, M, N>&);
};


template <class T>
void CNE6SSM_spectrum_plotter::extract_spectrum(const CNE6SSM<T>& model)
{
   spectrum.clear();
   scale = model.get_scale();

   spectrum.push_back(TParticle("Glu", "\\tilde{g}", to_valarray(PHYSICAL(MGlu))));
   spectrum.push_back(TParticle("ChaP", "\\tilde{\\chi}^{'-}", to_valarray(PHYSICAL(MChaP))));
   spectrum.push_back(TParticle("VZp", "{Z'}", to_valarray(PHYSICAL(MVZp))));
   spectrum.push_back(TParticle("Sd", "\\tilde{d}", to_valarray(PHYSICAL(MSd))));
   spectrum.push_back(TParticle("Sv", "\\tilde{\\nu}", to_valarray(PHYSICAL(MSv))));
   spectrum.push_back(TParticle("Su", "\\tilde{u}", to_valarray(PHYSICAL(MSu))));
   spectrum.push_back(TParticle("Se", "\\tilde{e}", to_valarray(PHYSICAL(MSe))));
   spectrum.push_back(TParticle("SDX", "\\tilde{x}", to_valarray(PHYSICAL(MSDX))));
   spectrum.push_back(TParticle("hh", "h", to_valarray(PHYSICAL(Mhh))));
   spectrum.push_back(TParticle("Ah", "A^0", to_valarray(PHYSICAL(MAh))));
   spectrum.push_back(TParticle("Hpm", "H^-", to_valarray(PHYSICAL(MHpm))));
   spectrum.push_back(TParticle("Chi", "\\tilde{\\chi}^0", to_valarray(PHYSICAL(MChi))));
   spectrum.push_back(TParticle("Cha", "\\tilde{\\chi}^-", to_valarray(PHYSICAL(MCha))));
   spectrum.push_back(TParticle("FDX", "x", to_valarray(PHYSICAL(MFDX))));
   spectrum.push_back(TParticle("SHI0", "h^{0,Inert}", to_valarray(PHYSICAL(MSHI0))));
   spectrum.push_back(TParticle("SHIPM", "h^{-,Inert}", to_valarray(PHYSICAL(MSHIPM))));
   spectrum.push_back(TParticle("ChaI", "\\tilde{\\chi}^{-,Inert}", to_valarray(PHYSICAL(MChaI))));
   spectrum.push_back(TParticle("ChiI", "\\tilde{\\chi}^{0,Inert}", to_valarray(PHYSICAL(MChiI))));
   spectrum.push_back(TParticle("SHp0", "H^{'0}", to_valarray(PHYSICAL(MSHp0))));
   spectrum.push_back(TParticle("SHpp", "H^{'-}", to_valarray(PHYSICAL(MSHpp))));
   spectrum.push_back(TParticle("ChiP", "\\tilde{\\chi}^{'0}", to_valarray(PHYSICAL(MChiP))));

   if (model.do_calculate_sm_pole_masses()) {
      spectrum.push_back(TParticle("Fd", "d", to_valarray(PHYSICAL(MFd))));
      spectrum.push_back(TParticle("Fe", "e", to_valarray(PHYSICAL(MFe))));
      spectrum.push_back(TParticle("Fu", "u", to_valarray(PHYSICAL(MFu))));
      spectrum.push_back(TParticle("Fv", "\\nu", to_valarray(PHYSICAL(MFv))));
      spectrum.push_back(TParticle("VG", "g", to_valarray(PHYSICAL(MVG))));
      spectrum.push_back(TParticle("VP", "\\gamma", to_valarray(PHYSICAL(MVP))));
      spectrum.push_back(TParticle("VWm", "W^-", to_valarray(PHYSICAL(MVWm))));
      spectrum.push_back(TParticle("VZ", "Z", to_valarray(PHYSICAL(MVZ))));

   }
}

template <class Scalar, int M, int N>
std::valarray<double> CNE6SSM_spectrum_plotter::to_valarray(const Eigen::Array<Scalar, M, N>& v)
{
   return std::valarray<double>(v.data(), v.size());
}

} // namespace flexiblesusy

#endif
