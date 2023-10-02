{ sources ? import ./nix/sources.nix

, pkgs ? import sources.nixpkgs {}

}:



pkgs.mkShell {
  packages = [
    pkgs.texlive.combined.scheme-full
    pkgs.biber
    pkgs.gnumake
  ];
}